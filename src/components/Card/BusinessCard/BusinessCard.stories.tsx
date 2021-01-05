import { Story, Meta } from '@storybook/react/types-6-0';

import {BusinessCardProps, BusinessCard as BusinessCardComponent} from './BusinessCard';

export default {
    title: 'Components/Card',
    component: BusinessCardComponent,
} as Meta;

const Template: Story<BusinessCardProps> = (args) => <BusinessCardComponent {...args} />;

export const BusinessCard = Template.bind({});
BusinessCard.args = {
    isSender: true,
    name: 'Rishabh Controls',
    gst: '24ABNPN1124A1ZA',
    address: `Address #1
    Address #2`,
    phone: 1234567890
}